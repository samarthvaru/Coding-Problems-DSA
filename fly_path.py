"""
xCoordinate, represents the N coordinates on x-axis.
yCoordinate, represents the M coordinates on y-axis.
"""
def funcDrop(x_coordinates, y_coordinates):
	# Write your code here
    unique_coordinates = set(zip(x_coordinates, y_coordinates))
    
    # Check if there are less than two unique coordinates
    if len(unique_coordinates) < 2:
        return 0

    max_points = 0

    for i in range(len(x_coordinates)):
        for j in range(i + 1, len(x_coordinates)):
            if x_coordinates[i] == x_coordinates[j]:
                # Calculate the number of points covered by flying horizontally
                count = sum(1 for coord in unique_coordinates if coord[0] == x_coordinates[i])
                max_points = max(max_points, count)
            elif y_coordinates[i] == y_coordinates[j]:
                # Calculate the number of points covered by flying vertically
                count = sum(1 for coord in unique_coordinates if coord[1] == y_coordinates[i])
                max_points = max(max_points, count)

    return max_points

def main():
	# input for xCoordinate
	xCoordinate = []
	xCoordinate_size  = int(raw_input())
	xCoordinate = list(map(int,raw_input().split()))
	# input for yCoordinate
	yCoordinate = []
	yCoordinate_size  = int(raw_input())
	yCoordinate = list(map(int,raw_input().split()))
	
	result = funcDrop(xCoordinate, yCoordinate)
	print(result)

if __name__ == "__main__":
	main()