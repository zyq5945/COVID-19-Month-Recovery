import os
import time
import sys
import pandas as pd
from itertools import groupby
from operator import itemgetter


def data_is_num(v):
    return v != ''


def data_fmt(v):
    return int(v) if data_is_num(v) else ''


def data_div(v1, v2):
    return '' if v2 == 0 or not data_is_num(v1) or not data_is_num(v2) else v1/v2


def data_add(v1, v2):
    return data_fmt(v1) + data_fmt(v2) if data_is_num(v1) and data_is_num(v2) else ''


def data_dec(v1, v2):
    return data_fmt(v1) - data_fmt(v2) if data_is_num(v1) and data_is_num(v2) else ''


def data_dec_flt(v1, v2):
    return v1 - v2 if data_is_num(v1) and data_is_num(v2) else ''


def data_max(v1, v2):
    if data_is_num(v1) and data_is_num(v2):
        return max(v1, v2)
    if data_is_num(v1):
        return v1
    if data_is_num(v2):
        return v2
    return ''


def filter_global(df):
    total = df.query("Subregion.isna()")
    subregion = df.query("Subregion.notna()")
    all_sum = subregion.groupby(subregion['Region']).sum()
    empty = {'Region': '', 'Confirmed': '', 'Deaths': '', 'Recovered': ''}
    list = []
    for index, row in all_sum.iterrows():
        row = dict(row)
        tl = total[total['Region'] == index]
        old = empty if len(tl) != 1 else tl.iloc[0]
        row['Region'] = index
        row['Subregion'] = ""
        row['Confirmed'] = data_max(old['Confirmed'], row['Confirmed'])
        row['Deaths'] = data_max(old['Deaths'], row['Deaths'])
        row['Recovered'] = data_max(old['Recovered'], row['Recovered'])

        list.append(row)

    df = df.query("Region != 'US'")

    df = df.append(pd.DataFrame(list), ignore_index=True)
    return df


def read_data(file, names, is_global):
    if not os.path.exists(file):
        return []

    df = pd.read_csv(file)
    df = df.rename(columns=lambda x: x if x not in names else names[x])

    df = df[['Region', 'Subregion', 'Confirmed', 'Deaths', 'Recovered']]

    df['Subregion'][df['Region'] == df['Subregion']] = ''
    df = df.replace("Recovered", '')
    df = df.replace("Mainland China", 'China')

    if is_global:
        df = filter_global(df)
    else:
        df = df.query("Subregion.notna()")

    df = df.fillna('')
    df = df.sort_values(['Confirmed', 'Deaths', 'Recovered'], ascending=[False, False, False])
    df.drop_duplicates(subset=['Region', 'Subregion'], keep='first', inplace=True)
    return df.to_dict(orient='records')


def write_csv(file, datas):
    path = os.path.join(os.path.dirname(file),
                        os.path.splitext(os.path.basename(file))[0])

    columns = ['Index', 'Region', 'Subregion', 'Stage', 'Confirmed', 'Deaths', 'Recovered',
               'Stage_Confirmed', 'Stage_Deaths', 'Stage_Recovered',
               'Stage_Treated%', 'Stage_Deaths%', 'Stage_Recovered%',
               'Stage_Treated', 'Recovered_Change']

    pd.DataFrame(datas).to_csv(file, index=False, columns=columns)
    groups = groupby(datas, lambda x: '%s%s%s.csv' % (x['Region'], '' if x['Subregion'] == '' else '/', x['Subregion']))
    for key, group in groups:
        group = list(group)
        if len(group) <= 1:
            continue
        name = key.replace("*", "")
        file = os.path.join(path, name)
        cur_path = os.path.dirname(file)
        if not os.path.exists(cur_path):
            os.makedirs(cur_path)
        pd.DataFrame(group).to_csv(file, index=False, columns=columns)


def get_csv_files(path):
    files = os.listdir(path)
    files = [f for f in files if f.endswith('.csv') and '-' in f]
    return files


def fill_data(last, current):
    last.setdefault('Stage_Treated', '')
    last.setdefault('Stage_Recovered%', '')

    current['Stage_Confirmed'] = data_dec(current['Confirmed'], last['Treated'])
    current['Stage_Deaths'] = data_dec(current['Deaths'], last['Deaths'])
    current['Stage_Recovered'] = data_dec(current['Recovered'], last['Recovered'])
    current['Stage_Treated'] = data_dec(current['Treated'], last['Treated'])

    current['Stage_Treated%'] = data_div(current['Stage_Treated'], current['Stage_Confirmed'])
    current['Stage_Deaths%'] = data_div(current['Stage_Deaths'], current['Stage_Treated'])
    current['Stage_Recovered%'] = data_div(current['Stage_Recovered'], current['Stage_Treated'])

    current['Recovered_Change'] = data_dec_flt(current['Stage_Recovered%'], last['Stage_Recovered%'])
    return current


def make_data(key, index, names, file, is_global):
    datas = read_data(file, names, is_global)

    for item in datas:
        item['Stage'] = key
        item['Index'] = index
        item['Confirmed'] = data_fmt(item['Confirmed'])
        item['Deaths'] = data_fmt(item['Deaths'])
        item['Recovered'] = data_fmt(item['Recovered'])
        item['Treated'] = data_add(item['Recovered'], item['Deaths'])
    return datas


def get_data_indexs(files, step):
    if step > 0:
        size = len(files)
        list = [i for i in range(step - 1, size, step)]
        last = list[-1]
        offset = size - 1
        if last < offset:
            list.append(offset)
    else:
        groups = groupby(files, lambda x: '%04d-%02d' % (x.tm_year, x.tm_mon))
        list = [files.index(max(group)) for _, group in groups]

    return list


def get_all_data(root_global, root_usa, names, step):
    files = get_csv_files(root_global)
    files = [time.strptime(x.split('.')[0], '%m-%d-%Y') for x in files]
    files.sort()

    datas = []
    index = 1
    for i in get_data_indexs(files, step):
        tm = files[i]
        key = '%04d-%02d-%02d' % (tm.tm_year, tm.tm_mon, tm.tm_mday)
        file = '%02d-%02d-%04d.csv' % (tm.tm_mon, tm.tm_mday, tm.tm_year)
        list = make_data(key, index, names, os.path.join(root_global, file), True)
        datas.extend(list)
        list = make_data(key, index, names, os.path.join(root_usa, file), False)
        datas.extend(list)
        index += 1

    datas = sorted(datas, key=itemgetter('Region', 'Subregion', 'Index'))
    last = empty = {'Region': '', 'Subregion': '', 'Confirmed': 0, 'Deaths': 0, 'Recovered': 0, 'Treated': 0}
    for item in datas:
        tmp = empty if last['Region'] != item['Region'] or last['Subregion'] != item['Subregion'] else last
        fill_data(tmp, item)
        last = item

    return datas


def main():
    argv = sys.argv
    argn = len(argv)
    root = './' if argn < 2 else argv[1]
    out_dir = './' if argn < 3 else argv[2]
    step = 0 if argn < 4 else int(argv[3])

    root_global = os.path.join(root, 'csse_covid_19_data/csse_covid_19_daily_reports')
    root_usa = os.path.join(root, 'csse_covid_19_data/csse_covid_19_daily_reports_us')

    if not os.path.exists(root_usa):
        print('input data dir is error:%s' % root)
        return

    if not os.path.exists(out_dir):
        print('output data dir is error:%s' % out_dir)
        return

    names = {'Country/Region': 'Region',
             'Country_Region': 'Region',
             'Province/State': 'Subregion',
             'Province_State': 'Subregion'}

    datas = get_all_data(root_global, root_usa, names, step)
    write_csv(os.path.join(out_dir, 'COVID-19.csv'), datas)


if __name__ == '__main__':
    main()
