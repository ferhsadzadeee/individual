def acmTeam(topics):
    topic_ints = list(map(lambda x: int(x, 2), topics))

    max_topics = 0
    team_count = 0

    for i in range(len(topic_ints)):
        for j in range(i + 1, len(topic_ints)):
            combined = topic_ints[i] | topic_ints[j]
            known = bin(combined).count('1')

            if known > max_topics:
                max_topics = known
                team_count = 1
            elif known == max_topics:
                team_count += 1

    return [max_topics, team_count]


n, m = 4, 5
topics = [
    "10101",
    "11100",
    "11010",
    "00101"
]

print(acmTeam(topics))