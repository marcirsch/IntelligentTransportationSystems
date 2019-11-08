AR_X_OFFSET = -10
AR_Y_OFFSET = -15
AR_Z_OFFSET = 10
AR_DISTANCE = 5


def write_base(f):
    f.write("""<?xml version="1.0" ?>


<sdf version="1.5">
  <world name="default">

    <!-- A global light source -->
    <include>
      <uri>model://sun</uri>
    </include>

    <!-- A ground plane -->
    <include>
      <uri>model://ground_plane</uri>
    </include>
    """)

def write_end(f):
    f.write("""
  </world>
</sdf>""")

def write_sch(f):
    f.write("""<!-- Schonherz  -->
    <include>
      <uri>model://schonherz</uri>
      <pose>-10.5 0 0 0 0 0</pose>
    </include>""")

def generate_ar_codes(f):
    ar_cntr = 0
    for floor in range(10):

        z_offset = AR_Z_OFFSET + AR_DISTANCE*floor
        for row in range(7):
            name = str(ar_cntr).zfill(5)
            print(name)
            ar_cntr += 1
            
            y_offset = AR_Y_OFFSET + AR_DISTANCE*row

            f.write("""
        <include>
            <uri>model://""" + name + """</uri>
            <pose>""" + str(AR_X_OFFSET) + """ """ + str(y_offset) + """ """ + str(z_offset)+ """ 0 0 0</pose>
        </include>
            """)



f=open("output/schonherz.world", "w")

write_base(f)
write_sch(f)
generate_ar_codes(f)
write_end(f)
f.close()

