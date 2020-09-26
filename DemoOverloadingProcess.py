class Shape:
    def area(self, x=None, y=None):
        if x!=None and y!=None:
            return x*y
        elif x!=None:
            return x*x
        else :
            return 0


sh= Shape()
print("Area =", sh.area())
print("Area  of square =", sh.area(4))
print("Area  of rectangle=", sh.area(4,6))

# HPE Policy prohibits employees from engaging in 
# activities that pose a conflict(s) 
# of interest for HPE such as: Outside 
# employment with or receiving compensation from a customer,
#  business partner, supplier, or competitor; 
# Significant financial interest in a customer, business partner, 
# supplier, or competitor held by you or a family member; Conducting business with a customer, 
# business partner, supplier, or channel partner when someone you have a close personal 
# or family relationship has a substantial role in that company; 
# Close personal relationships between employees in the same organization. To identify situations 
# that may pose a conflict and be inconsistent with this policy, 
# please advise if you would be engaging in any of the above listed 
# situations or activities during your HPE employment if you were hired into the 
# role for which you have applied.
# iska mltb samjha
    
            