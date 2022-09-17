import requests

url = "https://leetcode.com/graphql"
query = """
query questionOfToday {
	activeDailyCodingChallengeQuestion {
		date
		userStatus
		link
		question {
			acRate
			difficulty
			freqBar
			frontendQuestionId: questionFrontendId
			isFavor
			paidOnly: isPaidOnly
			status
			title
			titleSlug
			hasVideoSolution
			hasSolution
			topicTags {
				name
				id
				slug
			}
		}
	}
}
"""


def fetchDailyCodingChallenge(url=url, query=query):
    print("Sending request...")

    try:
        response = requests.post(url, json={"query": query})
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    # dict
    result = response.json()
    return result


dailyQuestion = fetchDailyCodingChallenge()

# def getQuestionName():


def getLink(data=dailyQuestion):
    leetcode_url = "https://leetcode.com"
    return leetcode_url + data["data"]["activeDailyCodingChallengeQuestion"]["link"]


def getDate(data=dailyQuestion):
    return data["data"]["activeDailyCodingChallengeQuestion"]["date"]


def getDifficulty(data=dailyQuestion):
    return data["data"]["activeDailyCodingChallengeQuestion"]["question"]["difficulty"]


def isPaidOnly(data=dailyQuestion):
    return data["data"]["activeDailyCodingChallengeQuestion"]["question"]["paidOnly"]


def getQuestionNumber(data=dailyQuestion):
    return data["data"]["activeDailyCodingChallengeQuestion"]["question"][
        "frontendQuestionId"
    ]


def getQuestionTitle(data=dailyQuestion):
    return data["data"]["activeDailyCodingChallengeQuestion"]["question"]["title"]


def getHints(data=dailyQuestion):
    topicTags = data["data"]["activeDailyCodingChallengeQuestion"]["question"][
        "topicTags"
    ]

    hints = ""
    for i, element in enumerate(topicTags):
        if i < (len(topicTags) - 1):
            hints += element["name"] + " | "
        else:
            hints += element["name"]

    return hints


def previewDateAndLevel():
    return getDate() + ": " + getDifficulty()


def previewTitle():
    return getQuestionNumber() + ": " + getQuestionTitle()


# print(getLink())
# print(getDate())
# print(getDifficulty())
# print(isPaidOnly())
# print(getHints())
# print(dailyQuestion)
