Summary:	An X Window System based news reader.
Name:		xrn
Version:	9.01
Release:	3
Copyright:	Distributable
Group:		Applications/News
Source:		ftp://ftp.x.org/contrib/applications/xrn/%{name}-%{version}.tgz
Patch0:		xrn-rh.patch
Patch1:		xrn-glibc.patch 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
A simple Usenet News reader for the X Window System.  Xrn allows you to
point and click your way through reading, replying and posting news
messages.

Install the xrn package if you need a simple news reader for X.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
xmkmf
%{__make} CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
	CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xrn <<EOF
xrn name "xrn"
xrn description "X News Reader"
xrn group Utilities/News
xrn exec "xrn &"
EOF

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/xrn

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xrn
%config %{_libdir}/X11/app-defaults/XRn
%config /etc/X11/wmconfig/xrn
