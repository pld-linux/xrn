Summary:	An X Window System based news reader.
Name:		xrn
Version:	9.01
Release:	3
Copyright:	Distributable
Group:		Applications/News
Group(de):	Applikationen/News
Group(pl):	Aplikacje/News
Source0:	ftp://ftp.x.org/contrib/applications/xrn/%{name}-%{version}.tgz
Patch0:		%{name}-rh.patch
Patch1:		%{name}-glibc.patch
Patch2:		%{name}-time.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	XFree86-devel

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
A simple Usenet News reader for the X Window System. Xrn allows you to
point and click your way through reading, replying and posting news
messages.

Install the xrn package if you need a simple news reader for X.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf
%{__make} CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
	CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cat > $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/xrn <<EOF
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
%config %{_sysconfdir}/X11/wmconfig/xrn
