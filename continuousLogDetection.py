log_file_path = '/var/log/apache2/access.log'
position_file_path = 'log_position.txt'
IntrusionOrAnomaly_path = 'IntrusionOrAnomaly.txt'

# Read the last position/line number from the position file
try:
    with open(position_file_path, 'r') as position_file:
        last_position = int(position_file.read())
except (ValueError, FileNotFoundError):
    last_position = 0

print(f"last position of logs: {last_position}")

# Open the log file and read the lines from the last position/line number onward
with open(log_file_path, 'r') as log_file:
    # Skip to the last position/line number
    for _ in range(last_position):
        log_file.readline()

    # Read the new lines
    new_logs = log_file.readlines()

# Update the last position/line number
last_position += len(new_logs)

# Write the updated position to the position file
with open(position_file_path, 'w') as position_file:
    position_file.write(str(last_position))

# Write the IntrusionOrAnomaly logs to a file
def precectedIntrusionOrAnomaly(log):
    with open(IntrusionOrAnomaly_path, 'w') as position_file:
        position_file.write(str(log))



# Predict the new logs and print the results
import predict
for log in new_logs:
    pred = predict.predict(log, "apache","./MODELS/attack_classifier_dt_1687847175.pkl")[0]
    if (pred == 1):
        print(f"For log {log} predected Anomaly or Intrusion")
        precectedIntrusionOrAnomaly(log)