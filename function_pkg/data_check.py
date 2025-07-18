# 基準外の温度を判定する関数
def check_temperature(temp):

    ref_temp = 35           # 基準温度を設定
    if temp > ref_temp:     
        return True         # 基準温度を超えた場合はTrueを返す 
    else:
        return False        # 基準温度以下の場合はFalseを返す

if __name__ == '__main__':
    temp = float(input("温度を入力してください: "))  # テストする温度を入力

    if check_temperature(temp):
        print('【危険】基準外の温度です。')
    else:
        print('温度は基準内です。')