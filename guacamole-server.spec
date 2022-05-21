Name:     guacamole-server
Version:  1.4.0
Release:  1%{?dist}
Summary:  Apache Guacamole is a clientless remote desktop gateway

License:  ASL 2.0
URL:      https://guacamole.apache.org/

# Apache Guacamole has a mirror redirector for its downloads
# You can get this tarball by following this link:
# https://apache.org/dyn/closer.lua/guacamole/1.4.0/source/guacamole-server-1.4.0.tar.gz?action=download
Source0:  guacamole-server-1.4.0.tar.gz
Source1:  guacd.conf

# Required:
BuildRequires: cairo-devel
BuildRequires: gcc
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpng-devel
BuildRequires: libtool
BuildRequires: libuuid-devel
BuildRequires: make
BuildRequires: systemd-rpm-macros
# Optional:
BuildRequires: ffmpeg-devel
BuildRequires: freerdp-devel
BuildRequires: libssh2-devel
BuildRequires: libvncserver-devel
BuildRequires: libvorbis-devel
BuildRequires: libwebp-devel
BuildRequires: libwebsockets-devel
BuildRequires: openssl-devel
BuildRequires: pango-devel
BuildRequires: pulseaudio-libs-devel

%package devel
Summary: Developnet fitles for guacd
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-ssh%{?_isa} = %{version}-%{release}
Requires: %{name}-telnet%{?_isa} = %{version}-%{release}
Requires: %{name}-rdp%{?_isa} = %{version}-%{release}
Requires: %{name}-vnc%{?_isa} = %{version}-%{release}
Requires: %{name}-kubernetes%{?_isa} = %{version}-%{release}

%package ssh
Summary: SSH supprt library for guacd
Requires: %{name}%{?_isa} = %{version}-%{release}

%package telnet
Summary: Telnet supprt library for guacd
Requires: %{name}%{?_isa} = %{version}-%{release}

%package rdp
Summary: RDP supprt library for guacd
Requires: %{name}%{?_isa} = %{version}-%{release}

%package vnc
Summary: VNC supprt library for guacd
Requires: %{name}%{?_isa} = %{version}-%{release}

%package kubernetes
Summary: Kubernetes supprt library for guacd
Requires: %{name}%{?_isa} = %{version}-%{release}

%description
Apache Guacamole is a clientless remote desktop gateway. It supports standard
protocols like VNC, RDP, and SSH.

%description devel
${summary}.

%description ssh
${summary}.

%description telnet
${summary}.

%description rdp
${summary}.

%description vnc
${summary}.

%description kubernetes
${summary}.

%prep
%setup -q

%build
./configure\
 --prefix=%{_usr}\
 --libdir=%{_libdir}\
 --runstatedir=%{_rundir}\
 --with-libuuid\
 --with-systemd-dir=%{_unitdir}\
 --enable-static=no
make LDFLAGS="%{?__global_ldflags}" CFLAGS="-DNDEBUG $RPM_OPT_FLAGS -Wno-error=unused-variable -Wno-error=deprecated-declarations -Wno-error=discarded-qualifiers" %{?_smp_mflags}

%install
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/guacamole/guacd.conf
make install DESTDIR=%{buildroot}

%files
%{_sysconfdir}/guacamole/guacd.conf
%{_bindir}/guacenc
%{_bindir}/guaclog
%{_libdir}/libguac.la
%{_libdir}/libguac.so
%{_libdir}/libguac.so.20
%{_libdir}/libguac.so.20.0.0
%{_unitdir}/guacd.service
%{_sbindir}/guacd
%{_mandir}/man1/guacenc.1*
%{_mandir}/man1/guaclog.1*
%{_mandir}/man5/guacd.conf.5*
%{_mandir}/man8/guacd.8*

%files devel
%{_includedir}/guacamole/*
%{_libdir}/libguac-client-*.so

%files ssh
%{_libdir}/libguac-client-ssh.la
%{_libdir}/libguac-client-ssh.so.*

%files telnet
%{_libdir}/libguac-client-telnet.la
%{_libdir}/libguac-client-telnet.so.*

%files rdp
%{_libdir}/libguac-client-rdp.la
%{_libdir}/libguac-client-rdp.so.*
%{_libdir}/freerdp2/libguac-common-svc-client.la
%{_libdir}/freerdp2/libguac-common-svc-client.so
%{_libdir}/freerdp2/libguacai-client.la
%{_libdir}/freerdp2/libguacai-client.so

%files vnc   
%{_libdir}/libguac-client-vnc.la
%{_libdir}/libguac-client-vnc.so.*

%files kubernetes
%{_libdir}/libguac-client-kubernetes.la
%{_libdir}/libguac-client-kubernetes.so.*

%changelog
* Sat May 21 2022 Marcin Skarbek <rpm@skarbek.name> - 1.4.0-1
- Initial package
