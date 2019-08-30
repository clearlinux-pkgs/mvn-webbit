#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-webbit
Version  : 0.4.14
Release  : 2
URL      : https://github.com/webbit/webbit/archive/v0.4.14.tar.gz
Source0  : https://github.com/webbit/webbit/archive/v0.4.14.tar.gz
Source1  : https://repo1.maven.org/maven2/org/webbitserver/webbit/0.4.14/webbit-0.4.14.jar
Source2  : https://repo1.maven.org/maven2/org/webbitserver/webbit/0.4.14/webbit-0.4.14.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mvn-webbit-data = %{version}-%{release}

%description
# Webbit - A Java event based WebSocket and HTTP server
## Getting it
Prebuilt JARs are available from the [central Maven repository](http://search.maven.org/#search%7Cga%7C1%7Cwebbit) or the [Sontatype Maven repository](https://oss.sonatype.org/content/repositories/releases/org/webbitserver/webbit/).

%package data
Summary: data components for the mvn-webbit package.
Group: Data

%description data
data components for the mvn-webbit package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/webbitserver/webbit/0.4.14
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/webbitserver/webbit/0.4.14/webbit-0.4.14.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/webbitserver/webbit/0.4.14
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/webbitserver/webbit/0.4.14/webbit-0.4.14.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/webbitserver/webbit/0.4.14/webbit-0.4.14.jar
/usr/share/java/.m2/repository/org/webbitserver/webbit/0.4.14/webbit-0.4.14.pom
