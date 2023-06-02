import random
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(base_dir, 'prefectural_office_location.txt')

def pref_location():
    pref_city_dict = {}
    pref_url_dict = {}

    with open(file_path, encoding='utf-8') as f:
        for i in f:
            txt_lines = i.rstrip().split(',')
            pref = txt_lines[0]
            city = txt_lines[1]
            url = txt_lines[2]

            #都道府県：県庁所在地となる辞書を作成
            if pref not in pref_city_dict:
                pref_city_dict[pref] = city
            
            #都道府県：URLとなる辞書を作成
            if url not in pref_url_dict:
                pref_url_dict[pref] = url

    #random.choiceを使うために当都道府県名が入ったlistを作成する
    pref_name = []
    for i in pref_city_dict.keys():
        pref_name.append(i)

    #ランダムに選択された都道府県名に対応する、都市名とURLを取得する。
    random_pref = random.choice(pref_name)

    city_name = pref_city_dict[random_pref]
    pref_url = pref_url_dict[random_pref]

    return random_pref, city_name, pref_url


if __name__ == '__main__':
    p, c, u = pref_location()
    print(p, c, u)
