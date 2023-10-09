def max_area(height):
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        h1 = height[left]
        h2 = height[right]

        width = right - left
        current_area = min(h1, h2) * width
        max_area = max(max_area, current_area)

        if h1 < h2:
            left += 1
        else:
            right -= 1
    return max_area
