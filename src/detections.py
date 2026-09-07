def detect_high_error_clients(client_counts, client_4xx_counts):
    suspicious_clients = []

    for client, errors in client_4xx_counts.items():
        total_requests = client_counts[client]

        if total_requests >= 20:
            error_rate = (errors / total_requests) * 100

            if error_rate >= 90:
                severity = "CRITICAL"
            elif error_rate >= 70:
                severity = "HIGH"
            elif error_rate > 50:
                severity = "MEDIUM"
            else:
                continue

            suspicious_clients.append(
                (client, total_requests, errors, error_rate, severity)
            )

    return suspicious_clients


def detect_excessive_404_clients(client_404_counts, threshold=20):
    suspicious_clients = []

    for client, errors in client_404_counts.items():
        if errors >= threshold:
            suspicious_clients.append(
                (client, errors)
            )

    return suspicious_clients

def detect_excessive_403_clients(client_403_counts, threshold=5):
    suspicious_clients = []

    for client, errors in client_403_counts.items():
        if errors >= threshold:
            suspicious_clients.append(
                (client, errors)
            )

    return suspicious_clients

def detect_excessive_403_clients(client_403_counts, threshold=5):
    suspicious_clients = []

    for client, errors in client_403_counts.items():
        if errors >= threshold:
            suspicious_clients.append(
                (client, errors)
            )

    return suspicious_clients