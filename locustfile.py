from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    host = "http://localhost:4173"
    wait_time = between(1, 5)  

    @task
    def load_homepage(self):
        self.client.get("/") 

    @task
    def load_logo(self):
        self.client.get("/src/assets/logo.png") 

