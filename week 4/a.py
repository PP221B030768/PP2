from datetime import datetime, timedelta
current = datetime.now().date()
ago = timedelta(5)
res = current - ago
print(res)