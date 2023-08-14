import csv
import time


def gc_file_transform(gene_file_path):
    # 生成对应csv文件名称
    csv_file_name = gene_file_path.split("/")[-1].split(".")[0] + '.csv'
    create_new_csv_file(csv_file_name)


# 生成csv文件
def create_new_csv_file(csv_file_name):
    # 生成对应csv文件路径
    csv_file_path = "./csv/" + csv_file_name
    # 处理gc文件或csv行数
    csv_file_line_num = 0
    new_csv_file = open(csv_file_path, "x", newline='')
    print_process_info(0, csv_file_name, csv_file_line_num)
    csv_writer = csv.writer(new_csv_file)
    # 提取原gc文件数据
    for gene_file_line in open(gene_file_path, encoding='utf-8'):
        # tsv文件注释跳过
        if gene_file_line.startswith("##"):
            continue
        else:
            # 提取原gc文件每行数据
            gene_file_line_part = gene_file_line.split()
            # 写入csv文件
            csv_writer.writerow(gene_file_line_part)
            csv_file_line_num += 1
    new_csv_file.close()
    print_process_info(1, csv_file_name, csv_file_line_num)


def print_process_info(step, csv_file_name, csv_file_line_num):
    if step == 0:
        print("[" +
              time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +
              "] " +
              csv_file_name + " processing data...")
    else:
        print("[" +
              time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +
              "] " +
              csv_file_name + " data processing complete, total processed lines: "+
              str(csv_file_line_num))


def tsv_file_transform(gene_file_path):
    # 处理tsv文件或csv行数
    tsv_file_line_num = 0
    # 生成对应csv文件名称
    csv_file_name = gene_file_path.split("/")[-1].replace('.tsv', '') + '.csv'
    create_new_csv_file(csv_file_name)


def raw_file_transform(gene_file_path):
    raw_file_type =gene_file_path.split(".")[-1]
    if raw_file_type == 'gc':
        gc_file_transform(gene_file_path)
    elif raw_file_type == 'tsv':
        tsv_file_transform(gene_file_path)


if __name__ == '__main__':
    gene_file_path = input('Please input the path of Gene file: ')
    raw_file_transform(gene_file_path)
