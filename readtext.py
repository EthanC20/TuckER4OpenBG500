# import csv
#
#
# def load_data(data_dir, data_type="train", reverse=False):
#     file_path = f"{data_dir}/{data_type}.tsv"
#     data = []
#
#     with open(file_path, 'r', encoding='utf-8') as f:
#         reader = csv.reader(f, delimiter='\t')
#         for row in reader:
#             data.append(row)
#             if reverse:
#                 data.append([row[2], row[1] + "_reverse", row[0]])
#
#     return data
#
#
# def load_data1(data_dir, data_type="train", reverse=False):
#     with open("%s%s.txt" % (data_dir, data_type), "r") as f:
#         data = f.read().strip().split("\n")
#         data = [i.split() for i in data]
#         if reverse:
#             data += [[i[2], i[1] + "_reverse", i[0]] for i in data]
#     return data
#
#
# data_dir1 = "data/FB15k-237/"
# data_dir = "data/OpenBG500"
#
# test_data1 = load_data1(data_dir1, "train")
# test_data = load_data(data_dir, "train")
# print(test_data1[0])
# print(test_data[0])
