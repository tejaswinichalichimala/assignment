def chunk_data(lines, size=50):
    """
    Splits log lines into chunks
    """
    for i in range(0, len(lines), size):
        yield lines[i:i + size]