from infra.Repository.Share_Repository import ShareRepository

repo = ShareRepository()

data = repo.Select()

print(data)