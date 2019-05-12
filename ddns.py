import boto3
import urllib.request

client = boto3.client('route53')

host_name = 'example.com.'
hosted_zone_id = 'Route53 Zone Id Goes Here'

ip_address = urllib.request.urlopen('https://api.ipify.org').read()
ip6_address = urllib.request.urlopen('https://api6.ipify.org').read()

response = client.change_resource_record_sets(
    HostedZoneId=hosted_zone_id,
    ChangeBatch={
        'Comment': 'home ip address',
        'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': host_name,
                    'Type': 'A',
                    'TTL': 60,
                    'ResourceRecords': [
                        {
                            'Value': ip_address.decode()
                        },
                    ]
                }
            }
        ]
    }
)

response6 = client.change_resource_record_sets(
    HostedZoneId=hosted_zone_id,
    ChangeBatch={
        'Comment': 'home ip address',
        'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': host_name,
                    'Type': 'AAAA',
                    'TTL': 60,
                    'ResourceRecords': [
                        {
                            'Value': ip6_address.decode()
                        },
                    ]
                }
            }
        ]
    }
)
