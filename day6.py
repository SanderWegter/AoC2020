#!/usr/bin/python3
from shared import read_from_file_grouped

custom_forms = read_from_file_grouped('inputs/day6.txt')

def num_yes(forms):
  return sum([len(set(form_group.replace('\n', ''))) for form_group in forms])

def num_all_yes(forms):
  sum_yes = 0
  for form_group in forms:
    sum_yes += len(set.intersection(*[set(l) for l in form_group.split("\n")]))
  return sum_yes

print("Part 1:", num_yes(custom_forms))
print("Part 2:", num_all_yes(custom_forms))