from plyer import notification

def notifier(summary, body, icon):
	n = notification.notify(
		title = f'{summary}',
		message = f'{body}',
		app_icon = f'{icon}'
		)
	