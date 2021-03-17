with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    parsing_list = []
    remote_addr_spam = {}
    spam_counter = [0, None]
    for line in f:
        remote_addr = line.split()[0]
        parsing_line = (remote_addr, line.split()[5][1:], line.split()[6])
        parsing_list.append(parsing_line)
        if remote_addr not in remote_addr_spam:
            remote_addr_spam[remote_addr] = 0
        remote_addr_spam[remote_addr] += 1
        if remote_addr_spam[remote_addr] > spam_counter[0]:
            spam_counter[0] = remote_addr_spam[remote_addr]
            spam_counter[1] = remote_addr

print(parsing_list)
print(spam_counter)
