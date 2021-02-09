
import numpy as np
import pandas as pd
from datetime import datetime as dt
import itertools

# Read data
loc = "/Users/juandollaa/Desktop/Data Mining P2/Datasets"

notprocessedData1 = pd.read_csv(loc + '2000-01.csv')
notprocessedData2 = pd.read_csv(loc + '2001-02.csv')
notprocessedData3 = pd.read_csv(loc + '2002-03.csv')
notprocessedData4 = pd.read_csv(loc + '2003-04.csv')
notprocessedData5 = pd.read_csv(loc + '2004-05.csv')
notprocessedData6 = pd.read_csv(loc + '2005-06.csv')
notprocessedData7 = pd.read_csv(loc + '2006-07.csv')
notprocessedData8 = pd.read_csv(loc + '2007-08.csv')
notprocessedData9 = pd.read_csv(loc + '2008-09.csv')
notprocessedData10 = pd.read_csv(loc + '2009-10.csv')
notprocessedData11 = pd.read_csv(loc + '2010-11.csv')
notprocessedData12 = pd.read_csv(loc + '2011-12.csv')
notprocessedData13 = pd.read_csv(loc + '2012-13.csv')
notprocessedData14 = pd.read_csv(loc + '2013-14.csv')
notprocessedData15 = pd.read_csv(loc + '2014-15.csv')
notprocessedData16 = pd.read_csv(loc + '2015-16.csv')




def removingDate(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%d/%m/%y').date()
def restOfData(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%d/%m/%Y').date()
notprocessedData1.Date = notprocessedData1.Date.apply(removingDate)
notprocessedData2.Date = notprocessedData2.Date.apply(removingDate)
notprocessedData3.Date = notprocessedData3.Date.apply(restOfData)
notprocessedData4.Date = notprocessedData4.Date.apply(removingDate)
notprocessedData5.Date = notprocessedData5.Date.apply(removingDate)
notprocessedData6.Date = notprocessedData6.Date.apply(removingDate)
notprocessedData7.Date = notprocessedData7.Date.apply(removingDate)
notprocessedData8.Date = notprocessedData8.Date.apply(removingDate)
notprocessedData9.Date = notprocessedData9.Date.apply(removingDate)
notprocessedData10.Date = notprocessedData10.Date.apply(removingDate)
notprocessedData11.Date = notprocessedData11.Date.apply(removingDate)
notprocessedData12.Date = notprocessedData12.Date.apply(removingDate)
notprocessedData13.Date = notprocessedData13.Date.apply(removingDate)
notprocessedData14.Date = notprocessedData14.Date.apply(removingDate)
notprocessedData15.Date = notprocessedData15.Date.apply(removingDate)
notprocessedData16.Date = notprocessedData16.Date.apply(removingDate)



                      
relevantCol = ['Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR']

playingData1 = notprocessedData1[relevantCol]
playingData2 = notprocessedData2[relevantCol]
playingData3 = notprocessedData3[relevantCol]
playingData4 = notprocessedData4[relevantCol]
playingData5 = notprocessedData5[relevantCol]
playingData6 = notprocessedData6[relevantCol]
playingData7 = notprocessedData7[relevantCol]
playingData8 = notprocessedData8[relevantCol]
playingData9 = notprocessedData9[relevantCol]
playingData10 = notprocessedData10[relevantCol]
playingData11 = notprocessedData11[relevantCol]
playingData12 = notprocessedData12[relevantCol]
playingData13 = notprocessedData13[relevantCol]
playingData14 = notprocessedData14[relevantCol]
playingData15 = notprocessedData15[relevantCol]
playingData16 = notprocessedData16[relevantCol]


def goalsScored(playingInfo):
    teamnames = {}
    for i in playingInfo.groupby('HomeTeam').mean().T.columns:
        teamnames[i] = []
    for i in range(len(playingInfo)):
        HTGS = playingInfo.iloc[i]['FTHG']
        ATGS = playingInfo.iloc[i]['FTAG']
        teamnames[playingInfo.iloc[i].HomeTeam].append(HTGS)
        teamnames[playingInfo.iloc[i].AwayTeam].append(ATGS)
    GoalsScored = pd.DataFrame(data=teamnames, index = [i for i in range(1,39)]).T
    GoalsScored[0] = 0
    for i in range(2,39):
        GoalsScored[i] = GoalsScored[i] + GoalsScored[i-1]
    return GoalsScored

def concededGoals(playingInfo):
    teamnames = {}
    for i in playingInfo.groupby('HomeTeam').mean().T.columns:
        teamnames[i] = []
    for i in range(len(playingInfo)):
        ATGC = playingInfo.iloc[i]['FTHG']
        HTGC = playingInfo.iloc[i]['FTAG']
        teamnames[playingInfo.iloc[i].HomeTeam].append(HTGC)
        teamnames[playingInfo.iloc[i].AwayTeam].append(ATGC)
    GoalsConceded = pd.DataFrame(data=teamnames, index = [i for i in range(1,39)]).T
    GoalsConceded[0] = 0
    for i in range(2,39):
        GoalsConceded[i] = GoalsConceded[i] + GoalsConceded[i-1]
    return GoalsConceded

def getGoals(playingInfo):
    GC = concededGoals(playingInfo)
    GS = goalsScored(playingInfo)
    j = 0
    HTGS = []
    ATGS = []
    HTGC = []
    ATGC = []
    for i in range(380):
        ht = playingInfo.iloc[i].HomeTeam
        at = playingInfo.iloc[i].AwayTeam
        HTGS.append(GS.loc[ht][j])
        ATGS.append(GS.loc[at][j])
        HTGC.append(GC.loc[ht][j])
        ATGC.append(GC.loc[at][j])
        if ((i + 1)% 10) == 0:
            j = j + 1
    playingInfo['HTGS'] = HTGS
    playingInfo['ATGS'] = ATGS
    playingInfo['HTGC'] = HTGC
    playingInfo['ATGC'] = ATGC
    return playingInfo


playingData1 = getGoals(playingData1)
playingData2 = getGoals(playingData2)
playingData3 = getGoals(playingData3)
playingData4 = getGoals(playingData4)
playingData5 = getGoals(playingData5)
playingData6 = getGoals(playingData6)
playingData7 = getGoals(playingData7)
playingData8 = getGoals(playingData8)
playingData9 = getGoals(playingData9)
playingData10 = getGoals(playingData10)
playingData11 = getGoals(playingData11)
playingData12 = getGoals(playingData12)
playingData13 = getGoals(playingData13)
playingData14 = getGoals(playingData14)
playingData15 = getGoals(playingData15)
playingData16 = getGoals(playingData16)

def totalPoints(matches):
    matches_points = matches.applymap(scoringResults)
    for i in range(2,39):
        matches_points[i] = matches_points[i] + matches_points[i-1]
    matches_points.insert(column =0, loc = 0, value = [0*i for i in range(20)])
    return matches_points


def scoringResults(result):
    if result == 'W':
        return 3
    elif result == 'D':
        return 1
    else:
        return 0


def whichMatch(playingInfo):
    teamnames = {}
    for i in playingInfo.groupby('HomeTeam').mean().T.columns:
        teamnames[i] = []
    for i in range(len(playingInfo)):
        if playingInfo.iloc[i].FTR == 'H':
            teamnames[playingInfo.iloc[i].HomeTeam].append('W')
            teamnames[playingInfo.iloc[i].AwayTeam].append('L')
        elif playingInfo.iloc[i].FTR == 'A':
            teamnames[playingInfo.iloc[i].AwayTeam].append('W')
            teamnames[playingInfo.iloc[i].HomeTeam].append('L')
        else:
            teamnames[playingInfo.iloc[i].AwayTeam].append('D')
            teamnames[playingInfo.iloc[i].HomeTeam].append('D')
    return pd.DataFrame(data=teamnames, index = [i for i in range(1,39)]).T


def totalAggregation(playingInfo):
    matches = whichMatch(playingInfo)
    cum_pts = totalPoints(matches)
    HTP = []
    ATP = []
    j = 0
    for i in range(380):
        ht = playingInfo.iloc[i].HomeTeam
        at = playingInfo.iloc[i].AwayTeam
        HTP.append(cum_pts.loc[ht][j])
        ATP.append(cum_pts.loc[at][j])
        if ((i + 1)% 10) == 0:
            j = j + 1
    playingInfo['HTP'] = HTP
    playingInfo['ATP'] = ATP
    return playingInfo

playingData1 = totalAggregation(playingData1)
playingData2 = totalAggregation(playingData2)
playingData3 = totalAggregation(playingData3)
playingData4 = totalAggregation(playingData4)
playingData5 = totalAggregation(playingData5)
playingData6 = totalAggregation(playingData6)
playingData7 = totalAggregation(playingData7)
playingData8 = totalAggregation(playingData8)
playingData9 = totalAggregation(playingData9)
playingData10 = totalAggregation(playingData10)
playingData11 = totalAggregation(playingData11)
playingData12 = totalAggregation(playingData12)
playingData13 = totalAggregation(playingData13)
playingData14 = totalAggregation(playingData14)
playingData15 = totalAggregation(playingData15)
playingData16 = totalAggregation(playingData16)

def LastMatchesRecord(playingInfo,num):
    form = whichMatch(playingInfo)
    form_final = form.copy()
    for i in range(num,39):
        form_final[i] = ''
        j = 0
        while j < num:
            form_final[i] += form[i-j]
            j += 1           
    return form_final


def matchesToDataFrame(playingInformation):
    playingInformation = addLastMatchesRecord(playingInformation,1)
    playingInformation = addLastMatchesRecord(playingInformation,2)
    playingInformation = addLastMatchesRecord(playingInformation,3)
    playingInformation = addLastMatchesRecord(playingInformation,4)
    playingInformation = addLastMatchesRecord(playingInformation,5)
    return playingInformation


def addLastMatchesRecord(playingInfo,num):
    form = LastMatchesRecord(playingInfo,num)
    h = ['M' for i in range(num * 10)]
    a = ['M' for i in range(num * 10)]
    j = num
    for i in range((num*10),380):
        ht = playingInfo.iloc[i].HomeTeam
        at = playingInfo.iloc[i].AwayTeam
        past = form.loc[ht][j]
        h.append(past[num-1])
        past = form.loc[at][j]
        a.append(past[num-1])
        if ((i + 1)% 10) == 0:
            j = j + 1
    playingInfo['HM' + str(num)] = h
    playingInfo['AM' + str(num)] = a
    return playingInfo


playingData1 = matchesToDataFrame(playingData1)
playingData2 = matchesToDataFrame(playingData2)
playingData3 = matchesToDataFrame(playingData3)
playingData4 = matchesToDataFrame(playingData4)
playingData5 = matchesToDataFrame(playingData5)
playingData6 = matchesToDataFrame(playingData6)
playingData7 = matchesToDataFrame(playingData7)
playingData8 = matchesToDataFrame(playingData8)
playingData9 = matchesToDataFrame(playingData9)
playingData10 = matchesToDataFrame(playingData10)
playingData11 = matchesToDataFrame(playingData11)
playingData12 = matchesToDataFrame(playingData12)
playingData13 = matchesToDataFrame(playingData13)
playingData14 = matchesToDataFrame(playingData14)
playingData15 = matchesToDataFrame(playingData15)
playingData16 = matchesToDataFrame(playingData16)


cols = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTGS', 'ATGS', 'HTGC', 'ATGC', 'HTP', 'ATP', 'HM1', 'HM2', 'HM3', 'HM4', 'HM5', 'AM1', 'AM2', 'AM3', 'AM4', 'AM5' ]

playingData1 = playingData1[cols]
playingData2 = playingData2[cols]
playingData3 = playingData3[cols]
playingData4 = playingData4[cols]
playingData5 = playingData5[cols]
playingData6 = playingData6[cols]
playingData7 = playingData7[cols]
playingData8 = playingData8[cols]
playingData9 = playingData9[cols]
playingData10 = playingData10[cols]
playingData11 = playingData11[cols]
playingData12 = playingData12[cols]
playingData13 = playingData13[cols]
playingData14 = playingData14[cols]
playingData15 = playingData15[cols]
playingData16 = playingData16[cols]

Standings = pd.read_csv(loc + "EPLStandings.csv")
Standings.set_index(['Team'], inplace=True)
Standings = Standings.fillna(18)

def lastMatch(playing_stat, Standings, year):
    HomeTeamLP = []
    AwayTeamLP = []
    for i in range(380):
        ht = playing_stat.iloc[i].HomeTeam
        at = playing_stat.iloc[i].AwayTeam
        HomeTeamLP.append(Standings.loc[ht][year])
        AwayTeamLP.append(Standings.loc[at][year])
    playing_stat['HomeTeamLP'] = HomeTeamLP
    playing_stat['AwayTeamLP'] = AwayTeamLP
    return playing_stat

playingData1 = lastMatch(playingData1, Standings, 0)
playingData2 = lastMatch(playingData2, Standings, 1)
playingData3 = lastMatch(playingData3, Standings, 2)
playingData4 = lastMatch(playingData4, Standings, 3)
playingData5 = lastMatch(playingData5, Standings, 4)
playingData6 = lastMatch(playingData6, Standings, 5)
playingData7 = lastMatch(playingData7, Standings, 6)
playingData8 = lastMatch(playingData8, Standings, 7)
playingData9 = lastMatch(playingData9, Standings, 8)
playingData10 = lastMatch(playingData10, Standings, 9)
playingData11 = lastMatch(playingData11, Standings, 10)
playingData12 = lastMatch(playingData12, Standings, 11)
playingData13 = lastMatch(playingData13, Standings, 12)
playingData14 = lastMatch(playingData14, Standings, 13)
playingData15 = lastMatch(playingData15, Standings, 14)
playingData16 = lastMatch(playingData16, Standings, 15)



def getMatches(playing_stat):
    j = 1
    MatchWeek = []
    for i in range(380):
        MatchWeek.append(j)
        if ((i + 1)% 10) == 0:
            j = j + 1
    playing_stat['MW'] = MatchWeek
    return playing_stat

playingData1 = getMatches(playingData1)
playingData2 = getMatches(playingData2)
playingData3 = getMatches(playingData3)
playingData4 = getMatches(playingData4)
playingData5 = getMatches(playingData5)
playingData6 = getMatches(playingData6)
playingData7 = getMatches(playingData7)
playingData8 = getMatches(playingData8)
playingData9 = getMatches(playingData9)
playingData10 = getMatches(playingData10)
playingData11 = getMatches(playingData11)
playingData12 = getMatches(playingData12)
playingData13 = getMatches(playingData13)
playingData14 = getMatches(playingData14)
playingData15 = getMatches(playingData15)
playingData16 = getMatches(playingData16)


playing_stat = pd.concat([playingData1,playingData2,playingData3,playingData4,playingData5,playingData6,playingData7,playingData8,playingData9,playingData10,playingData11,playingData12,playingData13,playingData14,playingData15,playingData16], ignore_index=True)


# Gets the form points.
def recordPoints(string):
    sum = 0
    for letter in string:
        sum += scoringResults(letter)
    return sum

playing_stat['HTFormPtsStr'] = playing_stat['HM1'] + playing_stat['HM2'] + playing_stat['HM3'] + playing_stat['HM4'] + playing_stat['HM5']
playing_stat['ATFormPtsStr'] = playing_stat['AM1'] + playing_stat['AM2'] + playing_stat['AM3'] + playing_stat['AM4'] + playing_stat['AM5']

playing_stat['HTFormPts'] = playing_stat['HTFormPtsStr'].apply(recordPoints)
playing_stat['ATFormPts'] = playing_stat['ATFormPtsStr'].apply(recordPoints)

# Identify Win/Loss Streaks if any.
def winStreak(string):
    if string[-3:] == 'WWW':
        return 1
    else:
        return 0
    
def winStreak5(string):
    if string == 'WWWWW':
        return 1
    else:
        return 0
    
def loseStreak(string):
    if string[-3:] == 'LLL':
        return 1
    else:
        return 0
    
def loseStreak5(string):
    if string == 'LLLLL':
        return 1
    else:
        return 0


playing_stat['HTWinStreak3'] = playing_stat['HTFormPtsStr'].apply(winStreak)
playing_stat['HTWinStreak5'] = playing_stat['HTFormPtsStr'].apply(winStreak5)
playing_stat['HTLossStreak3'] = playing_stat['HTFormPtsStr'].apply(loseStreak)
playing_stat['HTLossStreak5'] = playing_stat['HTFormPtsStr'].apply(loseStreak5)
playing_stat['ATWinStreak3'] = playing_stat['ATFormPtsStr'].apply(winStreak)
playing_stat['ATWinStreak5'] = playing_stat['ATFormPtsStr'].apply(winStreak5)
playing_stat['ATLossStreak3'] = playing_stat['ATFormPtsStr'].apply(loseStreak)
playing_stat['ATLossStreak5'] = playing_stat['ATFormPtsStr'].apply(loseStreak5)

playing_stat.keys()



playing_stat['HTGD'] = playing_stat['HTGS'] - playing_stat['HTGC']
playing_stat['ATGD'] = playing_stat['ATGS'] - playing_stat['ATGC']


playing_stat['DiffPts'] = playing_stat['HTP'] - playing_stat['ATP']
playing_stat['DiffFormPts'] = playing_stat['HTFormPts'] - playing_stat['ATFormPts']


playing_stat['DiffLP'] = playing_stat['HomeTeamLP'] - playing_stat['AwayTeamLP']


cols = ['HTGD','ATGD','DiffPts','DiffFormPts','HTP','ATP']
playing_stat.MW = playing_stat.MW.astype(float)

for col in cols:
    playing_stat[col] = playing_stat[col] / playing_stat.MW




def homeOrNot(string):
    if string == 'H':
        return 'H'
    else:
        return 'NH'
    
playing_stat['FTR'] = playing_stat.FTR.apply(homeOrNot)


playing_stat_test = playing_stat[5700:]


playing_stat.to_csv(loc + "final.csv")
playing_stat_test.to_csv(loc+"test.csv")



