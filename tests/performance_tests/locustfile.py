from locust import HttpUser, task


class project_perf_test(HttpUser):
    @task
    def points_display(self):
        self.client.get('/points')

    @task
    def show_summary(self):
        self.client.post('/showSummary',
                         data={"email": "john@simplylift.co"})

    @task
    def book(self):
        self.client.get('/book/Fall Classic/Simply Lift')

    @task
    def purchase_places(self):
        self.client.post('/purchasePlaces',
                         data={"competition": "Spring Festival",
                               "club": "Simply Lift",
                               "places": "3"})

    @task
    def logout(self):
        self.client.get('/logout')
