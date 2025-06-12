from src.data_processor import analyzeAnitabiStations

if __name__ == "__main__":
    subjectId = int(input("请输入作品 ID: "))
    analyzeAnitabiStations(subjectId, initialRadius=1000)