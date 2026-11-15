# Investigation Report | SSH Authentication Analysis

* **Environment:** Information Security Laboratory
* **Analyzed file:** `auth.log`
* **Log date:** November 8
* **Analysis type:** SSH Authentication Investigation

## 1. Incident Summary

During the analysis of the auth.log file, four failed SSH authentication attempts were identified, all originating from the IP address `192.0.2.45`.

Subsequently, a successful authentication was recorded for the user analyst, using the same IP address.

Following the login, an SSH session was opened, and the execution of the `/usr/bin/id` command through sudo was identified.

A few minutes later, another successful authentication was recorded, this time for the backup account, using an SSH public key and originating from the IP address `192.0.2.80`.

These events present potential indicators of suspicious activity, but are not sufficient on their own to confirm that the server was compromised.

## 2. Evidence Found

* 4 failed authentication attempts involving the users `admin`, `root`, and `analyst`.
* 2 successful authentication attempts involving the users `analyst` and `backup`.
* IP address `192.0.2.45` associated with the failed attempts and the login of `analyst`.
* IP address `192.0.2.80` associated with the login of `backup`.
* The user `analyst` executed `/usr/bin/id` using sudo.
* The `backup` account used a public key to authenticate and access the server.

## 3. Timeline

| Time | Event |
| - | - |
| 08:10:12 | First failed authentication attempt for admin |
| 08:10:18 | Second failed authentication attempt for admin |
| 08:10:24 | Failed authentication attempt for root |
| 08:11:02 | Failed authentication attempt for analyst |
| 08:11:15 | Successful authentication of analyst |
| 08:12:30 | SSH session opened for analyst |
| 08:14:05 | Execution of /usr/bin/id using sudo |
| 08:16:42 | SSH session closed for analyst |
| 08:20:01 | Successful public key authentication of backup |
| 08:20:10 | SSH session opened for backup |

## 4. Identified Suspicious Activities

### 4.1 Consecutive Authentication Attempts

The occurrence of four failed authentication attempts within approximately 50 seconds may indicate a brute-force attack or credential discovery attempt.

### 4.2 Successful Login Following Failed Attempts

The successful login to the `analyst` account, originating from the same IP address responsible for the previous attempts, deserves attention and needs to be validated.

### 4.3 Access to the `backup` Account

The subsequent authentication using an SSH public key requires further investigation to verify whether the key belongs to an authorized user.

It is important to emphasize that there is insufficient evidence to claim that this key was added by an attacker.

## 5. Conclusion

The analysis identified a sequence of events that deserves attention, particularly the consecutive failed authentication attempts followed by a successful login to the `analyst` account.

A subsequent login to the `backup` account was also identified, using public key authentication and a different IP address.

Although these events may indicate malicious activity, there is also the possibility that they represent legitimate access attempts.

Therefore, it is not possible to confirm that an intrusion or privilege escalation occurred based solely on the available logs.

## 6. Investigation Limitations

This investigation was conducted exclusively using the auth.log file provided in the laboratory.

The main limitations identified were:

* Lack of information to confirm the legitimacy of the IP addresses.
* Lack of a complete history of commands executed during the sessions.
* Lack of information regarding the origin and owner of the public key used by `backup`.
* Lack of additional system logs to correlate the events.
* Inability to determine whether the accesses were performed by legitimate users or unauthorized third parties.

> **Final Result:** Indicators of suspicious activity were identified, but there is insufficient evidence to confirm that the server was compromised.