# 打開檔案並讀取內容
with open('./input.txt', 'r') as f:
    Input = f.readlines()

# 解析第一行，初始化主程式列表
temp = Input[0].replace('\n', '').split(' ')
main = [[5, temp[0], temp[1], temp[2] if len(temp) == 3 else '']]

# 初始化巨集字典和巨集狀態
macro = {}
in_macro = [False, '']

line = 5
# 迭代處理每一行輸入
for i in Input[1:]:
    line += 5

    if i[0] == '.':
        continue

    i = i.replace('\n', '').split(' ')

    now = [line, *i[:3]] if len(i) == 3 else [line, '', *i[:2]]

    # 檢查是否進入巨集定義
    if now[2] == 'MACRO':
        in_macro = [True, now[1]]
        macro[now[1]] = [now[3].split(','), []]
        continue
    elif now[2] == 'MEND':
        in_macro = [False, '']
        continue

    # 如果在巨集中，將當前行添加到巨集中
    if in_macro[0]:
        macro[in_macro[1]][1].append(now)
    else:
        # 如果當前行是巨集調用
        if now[2] in macro:
            function_ = f'.{now[1]}' if now[1] else ''
            main.append(now.copy())

            # 解析巨集引數
            parms = dict(zip(macro[now[2]][0], now[3].split(',')))
            
            # 將巨集內容添加到主程式中
            macro[now[2]][1][0][1] = function_
            for n, j in enumerate(macro[now[2]][1]):
                j = j.copy()
                j[0] = f"{line}{chr(ord('a')+n)}"
                for k, v in parms.items():
                    j[3] = j[3].replace(k, v)

                main.append(j.copy())

        else:
            main.append(now)

# 輸出結果到 'output.txt'
output_file_path = 'output.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write("{:<10} {:<10} {:<10} {:<10}\n".format('行數', '', '原始碼', ''))
    for i in main:
        if i[1] == '.':
            output_file.write("{:<10} {:<10} {:<10} {:<39}\n".format(i[0], i[1], i[2], i[3]))
        else:
            output_file.write("{:<10} {:<10} {:<10} {:<10}\n".format(i[0], i[1], i[2], i[3]))

print(f"結果已寫入到 {output_file_path}")

