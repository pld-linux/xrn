Summary: An X Window System based news reader.
Name: xrn
Version: 9.01
Release: 3
Copyright: Distributable
Group: Applications/Internet
Source: ftp://ftp.x.org/contrib/applications/xrn/xrn-9.01.tgz
Patch0: xrn-rh.patch
Patch1: xrn-glibc.patch 
BuildRoot: /var/tmp/xrn-root

%description
A simple Usenet News reader for the X Window System.  Xrn allows you to
point and click your way through reading, replying and posting news
messages.

Install the xrn package if you need a simple news reader for X.

%prep
%setup -q -c
%patch0 -p1 -b .config
%patch1 -p1 -b .glibc

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xrn <<EOF
xrn name "xrn"
xrn description "X News Reader"
xrn group Utilities/News
xrn exec "xrn &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xrn
%config /usr/X11R6/lib/X11/app-defaults/XRn
%config /etc/X11/wmconfig/xrn
