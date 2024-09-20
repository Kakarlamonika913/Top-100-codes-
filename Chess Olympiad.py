x, y, z = map(int, input().split())
team_points = x + 0.5 * y
opponent_points = z + 0.5 * y
remaining_games = 4 - (x + y + z)
if team_points + remaining_games > opponent_points:
    print("YES")
else:
    print("NO")
