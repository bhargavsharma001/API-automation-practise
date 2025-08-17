class Resources:
    def get_all_breeds(self):
        return "/breeds/list/all"
    
    def get_random_breed(self):
        return "/breeds/image/random"
    
    def get_by_breed(self,type):
        return f"/breed/{type}/images"