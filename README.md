# iphonity

非公式 ipinfo.io スクレイパーモジュール

### 使い方

- as_info(ASN)
  
  AS番号から組織の情報を取得することができます。
  
  ```python
  import iphonity
  
  print(iphonity.as_info("AS15169"))
  #{'Country': ' United States', 'website': 'google.com', 'hosted_domains': '18,832,601', ...
  ```
  
  

- ip_info(IP)
  
  IPアドレスからホスト名などの情報を取得することができます
  
  
  ```python
  import iphonity 
  
  print(iphonity.ip_info("104.154.32.64"))
  #{'asn': 'AS396982 - Google LLC', 'hostname': '64.32.154.104.bc.googleusercontent.com' ...
  ```

- ip_range(ASN)
  
  組織に割り当てられているIPアドレスのサブネットが取得できます。
  
  ```python
  import iphonity
  
  print(iphonity.ip_range("AS15169"))
  #['104.154.0.0/15', '104.154.0.0/19', '104.154.128.0/19', ...
  ```

- locate(IP)
  
  IPアドレスから位置情報を取得できます。
  
  ```python
  import iphonity
  
  print(iphonity.locate("104.154.32.64"))
  #{'city': 'Council Bluffs', 'state': 'Iowa', 'country': ' United States' ...
  ```
  
  


