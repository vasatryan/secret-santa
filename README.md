# Secret Santa Automation Script 🎅 🎁

A Python script to automate Secret Santa assignments and email notifications. This script reads participant information from a CSV file, randomly assigns Secret Santas, and sends personalized emails to all participants.

## Features

- Random assignment of Secret Santa pairs (ensuring no one gets themselves)
- Automated email notifications with HTML formatting
- CSV-based participant management
- Rate limiting to prevent email server restrictions
- Error handling for email operations

## Prerequisites

- Python 3.x
- Access to an SMTP server
- CSV file with participant information

## Installation

1. Clone this repository or download the script
2. Install required Python packages (all packages used are part of Python's standard library)

## CSV File Format

Your CSV file should follow this format:

```csv
Name,Email
John Doe,john@example.com
Jane Smith,jane@example.com
```

## Configuration

Update the following variables in the script:

```python
file_path = "path/for/your/csv_file"  # Path to your CSV file
smtp_server = "smtp.example.com"       # Your SMTP server
smtp_port = 587                        # SMTP port number
sender_email = "example@email.com"     # Sender's email address
sender_password = "password"           # Sender's email password
```

## Usage

1. Prepare your CSV file with participants' information
2. Update the configuration variables in the script
3. Run the script:

```bash
python secret_santa.py
```

## Email Content

The script sends HTML-formatted emails containing:
- Recipient's Secret Santa assignment
- Event details (location, date)
- Gift budget information

## Functions

### `read_participants(file_path)`
Reads participant information from the CSV file.

### `assign_secret_santa(participants)`
Creates random Secret Santa assignments, ensuring no one gets themselves.

### `send_emails(santa_pairs, participants, smtp_server, smtp_port, sender_email, sender_password)`
Sends personalized emails to all participants with their assignments.

## Security Notes

- Do not commit the script with real SMTP credentials
- Consider using environment variables for sensitive information
- Ensure your SMTP connection is secure (TLS)

## Customization

You can customize the email template by modifying the HTML in the `send_emails` function:
- Change the email subject
- Modify the email body format
- Update event details
- Adjust the spending amount

## Error Handling

The script includes basic error handling for:
- Email sending failures
- CSV file reading issues
- Assignment conflicts

## Rate Limiting

The script includes a 2-second delay between emails to prevent server rate limiting issues. Adjust the `time.sleep(2)` value if needed.

## Contributing

Feel free to submit issues and enhancement requests!
