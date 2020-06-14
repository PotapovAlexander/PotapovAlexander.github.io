import pandas as pd
import os



def save_courses_to_excel(course_list):
    fn = 'tmp.xlsx'
    cols = ['Курс','Часы','Стоимость','Тип','Форма сдачи']
    df = pd.DataFrame(course_list, columns=cols)
    sum_row = df[['Стоимость']].sum(skipna = True)
    df_sum = pd.DataFrame(data=sum_row).T
    df_sum = df_sum.reindex(columns=df.columns)
    df = df.append(df_sum, ignore_index=True)
    df.tail()
    print(df)



    # print(df)
    # print(df[['Курс']])
    # df_sum = pd.DataFrame(data=sum_row)
    # print(df_sum)

    df.to_excel(fn, index=False)
    path = os.path.dirname(os.path.abspath(__file__)) + '/' + fn
    return path

if __name__=='__main__':
    data = [[1,2,30,4,5],[5,4,60,3,1]]
    save_courses_to_excel(data)