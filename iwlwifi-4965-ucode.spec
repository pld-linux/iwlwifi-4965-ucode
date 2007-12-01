Summary:	Microcode image for Intel Wireless WiFi Link 4965AGN Adapter
%define	_module	4965
Name:		iwlwifi-%{_module}-ucode
Version:	4.44.1.20
Release:	1
License:	distributable
Group:		System Environment/Kernel
Source0:	http://www.intellinuxwireless.org/iwlwifi/downloads/%{name}-%{version}.tgz
# Source0-md5:	6e5c396da265d79d5675fd345adf24cc
URL:		http://www.intellinuxwireless.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The file iwlwifi-4965-1.ucode provided in this package must be
present on your system in order for the Intel Wireless WiFi Link
4965AGN driver for Linux (iwlwifi-4965) to operate on your system.

The "-1" in the filename reflects an interface/architecture version number.
It will change only when changes in new uCode releases make the new uCode
incompatible with earlier drivers.

On adapter initialization, and at varying times during the uptime of
the adapter, the microcode is loaded into the RAM on the network
adapter.  The microcode provides the low level MAC features including
radio control and high precision timing events (backoff, transmit,
etc.) while also providing varying levels of packet filtering which can
be used to keep the host from having to handle packets that are not of
interest given the current operating mode of the device.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

install iwlwifi-%{_module}-*.ucode $RPM_BUILD_ROOT/lib/firmware
install LICENSE.%{name} $RPM_BUILD_ROOT/lib/firmware/%{name}-LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.%{name}
/lib/firmware/%{name}-LICENSE
/lib/firmware/*.ucode
