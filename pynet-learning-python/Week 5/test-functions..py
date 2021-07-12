# Functions!
# Always have have a retrun value

#define the function
def print_ip():
    print("My IP Address is 192.168.1.1")

#call the function
print_ip()
print_ip()

#pass an argument
def print_ip(ip_addr, username, password):
    print("My IP Address is {}".format(ip_addr))
    print(username)
    print(password)
    return

print_ip('10.1.1.0', 'admin', 'admin123')
print_ip('10.1.1.100', 'admin', 'admin123')
print_ip(ip_addr='10.10.10.10', username='read-only', password='mypass')

#pass an argument with default values
def print_ip(ip_addr, username='def-admin', password='def-pass'):
    print("My IP Address is {}".format(ip_addr))
    print(username)
    print(password)
    return

print_ip('10.1.1.0')

#pass a dictionary and use each element of the list
def print_ip(ip_addr, username='def-admin', password='def-pass'):
    print("My IP Address is {}".format(ip_addr))
    print(username)
    print(password)
    return

my_dict = {
    'ip_addr': '172.16.31.1',
    'username': 'admin_dict',
    'password': 'juniper123'
}

# Add a DOUBLE star
print_ip(**my_dict)

