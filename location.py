import numpy as np

def distance(lat1, long1, lat2, long2):
    R = 6371e3 #meters
    phi1 = lat1 * np.pi/180
    phi2 = lat2 * np.pi/180
    deltaPhi = phi1 - phi2
    deltaLong = (long1 - long2) * np.pi/180
    
    return np.arccos(np.sin(phi1)*np.sin(phi2) + np.cos(phi1)*np.cos(phi2)*np.cos(deltaLong))*R # in meters

uo_cern = distance(44.0448, -123.0726, 46.2022, 6.1457) #distance from UO to CERN
uo_oregonState = distance(44.0448, -123.0726,45.5234, -122.6762) #distance from UO to Oregon State U
uo_sydney = distance(44.0448, -123.0726,-33.8678,151.2073) #distance from UO to Sydney University 
uo_oxford = distance(44.0448, -123.0726,53.4809,-2.2374) #distance from UO to oxford
uo_cam = distance(44.0448, -123.0726,51.5085,-0.1257) #distance from UO to Cambridge
uo_yale = distance(44.0448, -123.0726,41.3081,-72.9282) #distnace from UO to Yale
uo_berkeley = distance(44.0448, -123.0726, 37.8716,-122.2728) #dsitance from UO to UCB
                     

print(uo_cern, uo_oregonState, uo_sydney, uo_oxford, uo_cam, uo_yale, uo_berkeley) #all in METERS
