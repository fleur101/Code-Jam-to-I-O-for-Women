#  You just bought a parcel of land that is K kilometers long; it is so narrow that, for the purposes of this problem, we will consider it to be a polyline that runs from west to east, varying in elevation. You know the elevations of the land (in meters) at K + 1 regularly spaced measurement marks M0, M1, ..., MK. These marks are 0, 1, ..., K km, respectively, from the western end.
# In this region, a wooden post denotes the boundary between two adjacent parcels of land. Wooden posts can only be placed at measurement marks, and there can be at most one post at each mark. Right now, there are two posts: one at the 0 km mark, and one at the K km mark. A measurement mark with a post is considered to be part of both of the parcels it demarcates, so your parcel of land includes all measurement marks between 0 and K km, inclusive.
# A parcel is considered desirable if it contains three measurement marks such that the west-most and east-most of those three marks are both strictly higher than the remaining one of the three marks, or both strictly lower than the remaining one of the three marks. People like some variation in their landscapes! Notice that these three marks are not necessarily consecutive, and the west-most and east-most of the three marks are not necessarily the west-most and east-most marks of the parcel.
# Consider an example with K = 5 and M0, M1, ..., MK = 5, 6, 6, 1, 2, 4. The measurement marks with elevations 5, 2, and 4 satisfy the condition, as do the measurement marks with elevations 6, 1, and 2. However, the measurement marks with elevations 6, 6, and 1 do not satisfy the condition, nor do the measurement marks with elevations 1, 2, and 4. Any three measurement marks that satisfy the condition make the whole parcel desirable; for example, a parcel containing the measurement marks 4 7 6 7 is desirable because of the first three values.
# Your parcel is desirable, but you think it may be possible to extract even more value from it! You want to add additional posts to this parcel to divide it up into multiple parcels, all of which must be desirable, since you do not want to waste any land. What is the largest number of posts you can add? 
T = int(input())
for i in range (1, T+1):
    numMarks = int(input())+1
    marks = [int(x) for x in input().split()]
    asc = False
    desc = False
    count = 0
    for j in range(1, numMarks):
        if (marks[j] > marks[j-1]):
            if (desc):
                desc = False
                asc = False
                count+=1
            else:
                asc = True
        elif (marks[j] < marks[j-1]):
            if (asc):
                asc = False
                desc = False 
                count+=1
            else:
                desc= True
    print('Case #{}: {}'.format(i, count-1))