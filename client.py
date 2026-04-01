import requests


res = requests.post("http://localhost:8000/tasks", json={"title": "Diadem", "description": "This is a test task", "completed": False},
                    headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4MGYyOTFiZS01ZWE4LTQ0MjktODE1Ni0zMTRkZTE1OGExYTIiLCJleHAiOjE3NzUwMjg2MzZ9.k0LtBWZRIw78T1PTe37Md0ywKtlss8B5NszMv___9hM"})

print(res.status_code)
print(res.text)