from collections import defaultdict


class Graph:
    def __init__(self, subjects):
        self.subjects = subjects
        self.graph = defaultdict(list)

    def add_edge(self, subject1, subject2):
        self.graph[subject1].append(subject2)
        self.graph[subject2].append(subject1)

    def graph_coloring(self):
        color_map = {}
        available_colors = set(range(1, len(self.subjects)+1))
        for subject in self.subjects:
            used_colors = set()
            for neighbor in self.graph[subject]:
                if neighbor in color_map:
                    used_colors.add(color_map[neighbor])

            available_colors = available_colors - used_colors

            if available_colors:
                color_map[subject] = min(available_colors)
            else:
                color_map[subject] = len(available_colors) + 1
                available_colors.add(color_map[subject])
        return color_map

    def get_minimum_time_slots(self):
        color_map = self.graph_coloring()
        return max(color_map.values())


subjects = [i for i in input("Enter the subjects: ").split()]# Math Physics Chemistry Biology ['Math', 'Physics', 'Chemistry', 'Biology']
# students = {
#     'Math': ['Alice', 'Bob', 'Charlie'], Alice Bob Charlie
#     'Physics': ['Alice', 'Charlie', 'David'], Alice Charlie David
#     'Chemistry': ['Bob', 'Charlie,' 'Eve'], Bob Charlie Eve
#     'Biology': ['Alice', 'David', 'Eve'] Alice David Eve
# }

students = {}
for subject in subjects:
    students[subject] = [name for name in input(f"Enter the name of students in {subject}: ").split()]
    
[print(f"{index}: {subject}") for index, subject in enumerate(subjects)]

graph = Graph(subjects)
N = int(input("No of edges: "))
print("Enter the edges [0 1]: ")
for i in range(N):
    sub1, sub2 = tuple([subjects[int(s)] for s in input().split()])
    graph.add_edge(sub1, sub2)
# graph.add_edge('Math', 'Physics')
# graph.add_edge('Math', 'Chemistry')
# graph.add_edge('Physics', 'Chemistry')
# graph.add_edge('Physics', 'Biology')

minimun_time_slots = graph.get_minimum_time_slots()
print(f"Minimum time slots required: {minimun_time_slots}")