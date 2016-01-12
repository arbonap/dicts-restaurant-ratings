# your code goes here
#open and feed in text file
#strip the whitespaces
#seperate restaurant name with split method via colon
#create empty dictionary
#set the dictionary key as restaurant name
#set the dictionary value as the restaurant rating
#
#sort 

def sort_restaurant_ratings(filename):
    list_of_restaurants = open(filename)
    restaurant_listing = {}
    
    for line in list_of_restaurants:
        line = line.rstrip()
        restaurant_details = line.split(':')
        restaurant_name = restaurant_details[0]
        restaurant_rating = restaurant_details[1]

        for restaurant in restaurant_name:
            restaurant_listing[restaurant_name] = restaurant_rating

    restaurant_tuple = restaurant_listing.items()
    #print restaurant_tuple

    final_sorted_list = sorted(restaurant_tuple)

        #print final_sorted_list
    for restaurant_entry in final_sorted_list:
        # print "Restaurant" + " " + restaurant_entry[0] + "has a rating of: " restaurant_entry[1]
        print "%s's rating is %s" % (restaurant_entry[0], restaurant_entry[1])

    #print "%s: %s" % (final_sorted_list[0], final_sorted_list[1])

        
        # for restaurant_name, restaurant_rating in restaurant_listing.items():
        #     print restaurant_name, restaurant_rating

sort_restaurant_ratings("scores.txt")

