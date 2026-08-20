from locust import HttpUser, task


class HelloWorldUser(HttpUser):

    def on_start(self):

        response = self.client.post(
            "/api/v1/token/create/",
            json={
                "email": "karimi.mohamad0011@gmail.com",
                "password": "m.k.o.1990",
            },
        )

        print("LOGIN STATUS:", response.status_code)
        print("LOGIN RESPONSE:", response.text)

        if response.status_code == 200:
            data = response.json()
            self.access_token = data.get("access")
        else:
            self.access_token = None

    @task
    def post_list(self):

        self.client.get(
            "/blog/api/v1/post/",
            headers={
                "Authorization": f"Bearer {self.access_token}"
            },
        )
    
    @task
    def category_list(self):

        self.client.get(
            "/blog/api/v1/category/",
            headers={
                "Authorization": f"Bearer {self.access_token}"
            },
        )