import argparse
import csv
import json

def extract_records_csv(input_file, output_file, n):
    records = []
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        for i, row in enumerate(reader):
            if i < n:
                records.append(row)
            else:
                break

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write the header row
        writer.writerows(records)

def extract_records_json(input_file, output_file, n):
    with open(input_file, 'r') as file:
        data = json.load(file)

    extracted_data = data[:n]

    with open(output_file, 'w') as file:
        json.dump(extracted_data, file, indent=4)
        
        
def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('entity',type=str)
    parser.add_argument('file', type=str)
    parser.add_argument('num', type=int)
    
    args = parser.parse_args()
    # print(args.entity)
    # print(args.file)
    # print(args.num)
    
    if args.entity=="Street":        
        if args.file=="csv":
            extract_records_csv(r"Street\data.csv", "Out/out_str.csv", args.num)
        elif args.file=="json":
            extract_records_json(r"Street\data.json", "Out/out_stu.json", args.num)
            
    elif  args.entity=="Student":
        if args.file=="csv":
            extract_records_csv(r"Student\data.csv", "Out/out_stu.csv", args.num)
        elif args.file=="json":
            extract_records_json(r"Student\data.json", "Out/out_stu.json", args.num)        
               
    
    
if __name__ == '__main__':
    main()

