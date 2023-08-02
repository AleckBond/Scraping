import csv
from collections import Counter

def count_word_frequency(csv_file_path):
    word_frequency = Counter()

    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Assuming the messages are in the first column of the CSV file, modify the index if needed.
            message = row[0]
            # Split the message into words by spaces (you can adjust this based on your data).
            words = message.split()
            # Update the word frequency counter.
            word_frequency.update(words)

    return word_frequency

def write_to_csv(word_frequency, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Frequency'])
        for word, frequency in word_frequency.most_common():
            writer.writerow([word, frequency])

def main():
    input_csv_file_path = 'chats.csv'  # Replace with the actual path to your CSV file.
    output_csv_file_path = 'frequency.csv'  # Output file path for frequency data.
    word_frequency = count_word_frequency(input_csv_file_path)

    # Write the words and their frequencies to the output CSV file.
    write_to_csv(word_frequency, output_csv_file_path)

if __name__ == "__main__":
    main()
