# Log Parsing

This repository contains a script for log parsing that reads data from stdin line by line and computes metrics based on the given input format. The script calculates and prints statistics after every 10 lines or upon keyboard interruption (CTRL + C). The statistics include the total file size and the number of lines by status code.

## Input Format

The input format for each log line is as follows:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

If the line does not match this format, it will be skipped.

## Script

The repository includes two Python scripts:

1. `0-generator.py`: This script is used to generate log lines and feed them into the log parsing script. It randomly generates 10,000 log lines with different IP addresses, dates, status codes, and file sizes.

2. `0-stats.py`: This script reads log lines from stdin, processes them, and computes the required metrics. The script prints the statistics after every 10 lines or upon a keyboard interruption.

## Output

The output of the log parsing script shows the following statistics:

- Total file size: The sum of all previous file sizes encountered in the log lines.
- Number of lines by status code: The count of each status code encountered in the log lines. The status codes are: 200, 301, 400, 401, 403, 404, 405, and 500. Status codes are printed in ascending order.

Please note that the output will vary as it is based on random log lines generated by the `0-generator.py` script.
