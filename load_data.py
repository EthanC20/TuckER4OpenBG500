import csv
import random

class Data:

    def __init__(self, data_dir="data/OpenBG500/", reverse=False):
        self.data_dir = data_dir
        self.reverse = reverse
        self.test_data = self.load_data("answer", sample=False)
        self.train_data = self.load_data("train", sample=True)
        self.valid_data = self.load_data("dev", sample=True)
        self.ensure_test_coverage()
        self.data = self.train_data + self.valid_data + self.test_data
        self.entities = self.get_entities(self.data)
        self.train_relations = self.get_relations(self.train_data)
        self.valid_relations = self.get_relations(self.valid_data)
        self.test_relations = self.get_relations(self.test_data)
        self.relations = self.train_relations + [i for i in self.valid_relations \
                                                 if i not in self.train_relations] + [i for i in self.test_relations \
                                                                                      if i not in self.train_relations]
        # 创建一个包含训练、验证和测试数据集中所有关系的列表，并确保每个关系只出现一次

    def load_data(self, data_type="train", sample=False):
        file_path = f"{self.data_dir}/{data_type}.tsv"
        data = []

        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='\t')
            rows = list(reader)
            if sample:
                rows = random.sample(rows, len(rows) // 50)
            for row in rows:
                data.append(row)
                if self.reverse:
                    data.append([row[2], row[1] + "_reverse", row[0]])

        return data

    def ensure_test_coverage(self):
        head_entities = set(d[0] for d in self.test_data)
        relations = set(d[1] for d in self.test_data)
        train_heads = set(d[0] for d in self.train_data)
        train_relations = set(d[1] for d in self.train_data)
        valid_heads = set(d[0] for d in self.valid_data)
        valid_relations = set(d[1] for d in self.valid_data)

        missing_train = [(h, r, t) for (h, r, t) in self.test_data if h not in train_heads or r not in train_relations]
        missing_valid = [(h, r, t) for (h, r, t) in self.test_data if h not in valid_heads or r not in valid_relations]

        self.train_data.extend(missing_train)
        self.valid_data.extend(missing_valid)

    def get_relations(self, data):
        relations = sorted(list(set([d[1] for d in data])))
        return relations

    def get_entities(self, data):
        entities = sorted(list(set([d[0] for d in data] + [d[2] for d in data])))
        return entities
