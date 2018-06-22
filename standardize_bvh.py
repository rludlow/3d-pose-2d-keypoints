import os

base = 'logs/cmu_files/'

# Standardized header
head_file = open(base + 'bvh_head.txt', 'r')
header = head_file.readlines()
head_file.close()

if __name__ == "__main__":
    bvh_subjects = [13,14,15,86]

    for subject in bvh_subjects:

        # Retrieve list of bvh files for given subject
        file_list = []
        original_dir = base + 'raw/{}/'.format(subject)
        standardized_dir = base + 'standardized/{}/'.format(subject)

        for root, dirs, files in os.walk(original_dir):
            file_list.extend(files)

        if not os.path.exists(standardized_dir):
            os.makedirs(standardized_dir)

        for file in file_list:

            original_bvh = open(original_dir + file, 'r')
            orig_lines = original_bvh.readlines()

            new_bvh = open(standardized_dir + file, 'w')

            # Write in standardized header
            new_bvh.writelines(header)

            # After passing the text "MOTION", copy every tenth line to new file
            write_now = False
            for i, line in enumerate(orig_lines):
                if write_now == True:
                    if i%10 == 0:
                        new_bvh.write(line)
                if line[0:6] == "MOTION":
                    write_now = True
