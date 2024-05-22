from skimage.metrics import structural_similarity
import cv2

def orb_sim(img1, img2):

    orb = cv2.ORB_create()

    # Detect key points amd descriptors
    kp_a, desc_a = orb.detectAndCompute(img1, None)
    kp_b, desc_b = orb.detectAndCompute(img2, None)

    # define the bruteforce matcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # perform matches
    matches = bf.match(desc_a, desc_b)

    # Look for similar regions with distance <= 50. Range goes from 0 to 100.(lower is better)
    similar_regions = [i for i in matches if i.distance <= 50]

    if len(matches) == 0:
        return 0
    
    return len(similar_regions) / len(matches)

def structural_sim(img1, img2):
    
    sim, diff = structural_similarity(img1, img2, full = True)

    return sim

# Images should have same size
image1 = cv2.imread('1.jpg', 0)
image2 = cv2.imread('2.jpg', 0)

orb_similarity = orb_sim(image1, image2)
s_sim = structural_sim(image1, image2)

print("Similarity using ORB: ", orb_similarity)
print("Similarity using SSIM: ", s_sim)
