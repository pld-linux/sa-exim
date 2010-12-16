Summary:	Exim SpamAssassin at SMTP time
Summary(pl.UTF-8):	SpamAssassin dla Exima działający w czasie SMTP
Name:		sa-exim
Version:	4.2.1
Release:	0.2
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://marc.merlins.org/linux/exim/files/%{name}-%{version}.tar.gz
# Source0-md5:	69268a81af366bc1b3e0c86000aed7db
Patch0:		%{name}-headers-location.patch
URL:		http://marc.merlins.org/linux/exim/sa.html
BuildRequires:	/usr/bin/links
BuildRequires:	exim-devel
Requires:	exim >= 2:4.52-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exim SpamAssassin at SMTP time.

%description -l pl.UTF-8
SpamAssassin dla Exima działający w czasie SMTP.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
SACONF="%{_sysconfdir}/mail/sa-exim.conf" \
	LDFLAGS="-shared -fPIC %{rpmldflags}" \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/mail,%{_libdir}/exim,%{_var}/spool/sa-exim}

install sa-exim-*.so $RPM_BUILD_ROOT%{_libdir}/exim/%{name}.so
install sa-exim.conf $RPM_BUILD_ROOT%{_sysconfdir}/mail/sa-exim.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc contrib/*.txt ACKNOWLEDGEMENTS CHANGELOG README* TODO
%attr(640,root,exim) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mail/sa-exim.conf
%attr(755,root,root) %{_libdir}/exim/%{name}.so
%dir %{_var}/spool/sa-exim
