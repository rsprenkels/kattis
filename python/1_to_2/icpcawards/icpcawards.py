def icpcawards(uni_teams):
    prize_winners = []
    universities_seen = set()
    for uni_team in uni_teams:
        university, team = uni_team.split()
        if university not in universities_seen:
            universities_seen.add(university)
            prize_winners.append(uni_team)
    return prize_winners[:12]


def test_1():
    sample_input = """30
Seoul ACGTeam
VNU LINUX
SJTU Mjolnir
VNU WINDOWS
NTU PECaveros
HUST BKJuniors
HCMUS HCMUSSerendipity
VNU UBUNTU
SJTU Metis
HUST BKDeepMind
HUST BKTornado
HCMUS HCMUSLattis
NUS Tourism
VNU DOS
HCMUS HCMUSTheCows
VNU ANDROID
HCMUS HCMUSPacman
HCMUS HCMUSGeomecry
UIndonesia DioramaBintang
VNU SOLARIS
UIndonesia UIChan
FPT ACceptable
HUST BKIT
PTIT Miners
PSA PSA
DaNangUT BDTTNeverGiveUp
VNU UNIXBSD
CanTho CTUA2LTT
Soongsil Team10deung
Soongsil BezzerBeater"""

    sample_output = """Seoul ACGTeam
VNU LINUX
SJTU Mjolnir
NTU PECaveros
HUST BKJuniors
HCMUS HCMUSSerendipity
NUS Tourism
UIndonesia DioramaBintang
FPT ACceptable
PTIT Miners
PSA PSA
DaNangUT BDTTNeverGiveUp"""

    assert icpcawards(sample_input.split('\n')[1:]) == sample_output.split('\n')

if __name__ == "__main__":
    num_lines = int(input())
    data = []
    for i in range(num_lines):
        data.append(input())
    for line in icpcawards(data):
        print(line)